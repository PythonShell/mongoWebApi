import dbsetup, datetime

dbsetup.board_table.drop() # remove collection board

test = {
    "bms": [
        { "bm": "soso" },
        { "bm": "Deatheart" },
        { "bm": "printk" }
    ],
    "boardName": "test",
    "zhName": "请在此测试",
    "totalTopics": 535
}

dbsetup.board_table.insert(test);
