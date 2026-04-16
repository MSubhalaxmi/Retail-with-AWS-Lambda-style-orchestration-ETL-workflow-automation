def authorize(role, action):
    permissions = {
        "admin": ["read", "write"],
        "user": ["read"]
    }
    return action in permissions.get(role, [])