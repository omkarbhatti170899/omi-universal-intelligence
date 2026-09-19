import hashlib, hmac, os, secrets, sqlite3, time, re
from pathlib import Path

DB=Path(os.getenv("OMI_DB","omi.db"))
SESSION_TTL=int(os.getenv("OMI_SESSION_TTL","86400"))
MIN_PASSWORD=8
EMAIL_RE=re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def db():
    DB.parent.mkdir(parents=True,exist_ok=True)
    c=sqlite3.connect(DB,timeout=5)
    c.execute("PRAGMA journal_mode=WAL")
    c.execute("PRAGMA foreign_keys=ON")
    c.execute("CREATE TABLE IF NOT EXISTS users(id TEXT PRIMARY KEY,email TEXT UNIQUE NOT NULL,password_hash TEXT NOT NULL,created_at INTEGER NOT NULL)")
    c.execute("CREATE TABLE IF NOT EXISTS sessions(token_hash TEXT PRIMARY KEY,user_id TEXT NOT NULL,expires_at INTEGER NOT NULL)")
    c.execute("CREATE TABLE IF NOT EXISTS memories(id INTEGER PRIMARY KEY AUTOINCREMENT,user_id TEXT NOT NULL,content TEXT NOT NULL,created_at INTEGER NOT NULL)")
    c.commit(); return c

def hash_password(password):
    salt=secrets.token_bytes(16)
    digest=hashlib.pbkdf2_hmac("sha256",password.encode(),salt,210000).hex()
    return salt.hex()+"$"+digest

def check_password(password,encoded):
    try:
        salt,digest=encoded.split("$",1)
        got=hashlib.pbkdf2_hmac("sha256",password.encode(),bytes.fromhex(salt),210000).hex()
        return hmac.compare_digest(got,digest)
    except Exception: return False

def create_user(email,password):
    email=email.lower().strip()
    if not EMAIL_RE.match(email) or len(password)<MIN_PASSWORD: raise ValueError("Invalid account details")
    c=db(); uid=secrets.token_urlsafe(12)
    try:
        c.execute("INSERT INTO users VALUES(?,?,?,?)",(uid,email,hash_password(password),int(time.time()))); c.commit()
    finally: c.close()
    return uid

def login(email,password):
    c=db(); row=c.execute("SELECT id,password_hash FROM users WHERE email=?",(email.lower().strip(),)).fetchone()
    if not row or not check_password(password,row[1]): c.close(); return None
    token=secrets.token_urlsafe(32); th=hashlib.sha256(token.encode()).hexdigest()
    c.execute("INSERT INTO sessions VALUES(?,?,?)",(th,row[0],int(time.time())+SESSION_TTL)); c.commit(); c.close()
    return token

def user_from_token(token):
    if not token: return None
    th=hashlib.sha256(token.encode()).hexdigest(); c=db()
    row=c.execute("SELECT user_id,expires_at FROM sessions WHERE token_hash=?",(th,)).fetchone()
    if row and row[1]<int(time.time()):
        c.execute("DELETE FROM sessions WHERE token_hash=?",(th,)); c.commit(); row=None
    c.close(); return row[0] if row else None

def remember(user_id,content):
    c=db(); c.execute("INSERT INTO memories(user_id,content,created_at) VALUES(?,?,?)",(user_id,str(content)[:2000],int(time.time()))); c.commit(); c.close()

def memories(user_id,limit=10):
    c=db(); rows=c.execute("SELECT content,created_at FROM memories WHERE user_id=? ORDER BY id DESC LIMIT ?",(user_id,max(1,min(int(limit),50)))).fetchall(); c.close()
    return [{"content":x[0],"created_at":x[1]} for x in rows]

def can_use_tool(user_id,tool):
    return bool(user_id) and tool in {"provider_generate","research"}
