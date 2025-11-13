#!/bin/bash
git add .gitignore

FAILURE_FILES="/var/log/syslog"
FAILURE_LOGIN_FILES="/var/log/auth.log"
TEST_FILES="test_files"
TEST_FILES1="test_files1"
LOG_DIR="storage"
mkdir -p $LOG_DIR

function Fault_Monitoring(){
    grep -E "Fail(ed)?|fail(ed)?|error|CRITICAL|critical|denied" $FAILURE_FILES |awk '{print $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11}' > $LOG_DIR/$TEST_FILES.csv
    grep -E "denied|unauthorized|fail(ed)?" $FAILURE_LOGIN_FILES |awk '{print $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11}' >> $LOG_DIR/$TEST_FILES.csv
}

    Fault_Monitoring
    python3 separator.py $LOG_DIR/$TEST_FILES.csv