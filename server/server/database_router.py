class DatabaseRouter:
    def db_for_read(self, model, **hints):
        # Điều hướng truy vấn đọc tới các database phụ (slave)
        import random
        return random.choice(['db01', 'db02', 'db03', 'db04'])

    def db_for_write(self, model, **hints):
        # Điều hướng truy vấn ghi về database chính (master)
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        # Cho phép quan hệ giữa các object nếu chúng thuộc các database đã cấu hình
        db_list = ['default', 'db01', 'db02', 'db03', 'db04']
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Chỉ cho phép migrate trên database chính
        return db == 'default'
