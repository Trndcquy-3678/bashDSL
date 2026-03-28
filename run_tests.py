import subprocess
import os
import sys

# The Test Runner (The Brains 🧠)
class TestRunner:
    def __init__(self, tests_dir='tests'):
        self.tests_dir = tests_dir
        self.python_path = '/data/data/com.termux/files/usr/bin/python3'

    def run_all(self):
        print("🚀 Running bashDSL Modular Vibe Check (The Test Suite) 💅")
        print("-" * 60)
        
        passed, failed = 0, 0
        for filename in sorted(os.listdir(self.tests_dir)):
            if filename.endswith('.shtemplate'):
                if self.run_test(filename):
                    passed += 1
                else:
                    failed += 1
        
        print("-" * 60)
        print(f"✨ Vibe check complete! (Passed: {passed}, Failed: {failed}) 💅")
        if failed > 0:
            sys.exit(1)

    def run_test(self, filename):
        filepath = os.path.join(self.tests_dir, filename)
        should_fail = filename.startswith('fail_')
        
        cmd = [self.python_path, 'main.py', filepath]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if should_fail:
            if result.returncode != 0:
                print(f"✅ PASSED: {filename} (Failed as expected: {result.stdout.strip()})")
                return True
            else:
                print(f"❌ FAILED: {filename} (Expected failure, but it passed! Oops.)")
                return False
        else:
            if result.returncode == 0:
                print(f"✅ PASSED: {filename} (Transpiled successfully! ✨)")
                return True
            else:
                print(f"❌ FAILED: {filename} (Unexpected error: {result.stdout.strip()})")
                return False

if __name__ == "__main__":
    runner = TestRunner()
    runner.run_all()
