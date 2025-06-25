def pytest_sessionstart(session):
    print("\n[SESSION START] Setting up test environment")

def pytest_sessionfinish(session, exitstatus):
    print("\n[SESSION END] Tearing down test environment")
