from app import app
c = app.test_client()
r = c.get('/')
print(r.status_code)
# print first 800 chars of response body for quick inspection
try:
    print(r.data.decode('utf-8')[:800])
except Exception:
    print(repr(r.data[:800]))
