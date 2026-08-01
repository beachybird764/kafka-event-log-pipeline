from configs.storage_config import AUDIT_PATH

def write_audit(df):
    (
        df.write
        .format("delta")
        .mode("append")
        .save(AUDIT_PATH)
    )