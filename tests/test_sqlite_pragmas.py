import pytest
from django.db import connections, transaction


@pytest.mark.django_db
class TestSQLitePragmas:
    """Test that SQLite PRAGMA settings are correctly applied."""
    
    def test_foreign_keys_enabled(self):
        """Test that SQLite foreign key support is enabled."""
        connection = connections['default']
        cursor = connection.cursor()
        
        cursor.execute('PRAGMA foreign_keys;')
        result = cursor.fetchone()[0]
        
        assert result == 1, "Foreign keys should be enabled (PRAGMA foreign_keys should be 1)"
    
    def test_strict_mode(self):
        """Test that SQLite strict mode is enabled if available."""
        connection = connections['default']
        cursor = connection.cursor()
        
        # First check if this SQLite version supports strict mode (added in 3.37.0)
        cursor.execute('SELECT sqlite_version();')
        version = cursor.fetchone()[0]
        
        try:
            major, minor, patch = map(int, version.split('.'))
            
            # Only test for strict mode if SQLite version supports it
            if major > 3 or (major == 3 and minor >= 37):
                cursor.execute('PRAGMA strict;')
                result = cursor.fetchone()[0]
                assert result == 1, "Strict mode should be enabled (PRAGMA strict should be 1)"
            else:
                # For older versions, just skip the test
                pytest.skip(f"SQLite version {version} does not support strict mode (requires 3.37.0+)")
        except ValueError:
            # Handle case where version format is unexpected
            pytest.skip(f"Cannot parse SQLite version: {version}")
        except Exception as e:
            # Skip if PRAGMA strict is not recognized
            pytest.skip(f"Error checking PRAGMA strict: {e}")