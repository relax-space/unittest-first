# unittest-first

## 开始
执行某一个方法
``` bash
python -m unittest -v tests/test_1.py -k TestUnit1.test_1
或者
python -m unittest -v tests.test_1.TestUnit1.test_1
```

## 调试
### 方法1
lauch.json文件: 点击vscode左边的debug图标, 创建lauch.json文件, 添加一个unittest节点,调试的时候选择这个节点
```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "py",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true
        },
        {
            "name": "unittest",
            "type": "python",
            "request": "launch",
            "purpose": ["debug-test"],
            "console": "integratedTerminal",
            "justMyCode": false,
            "module": "unittest",
            "args": [
                "-v",
                "tests/test_1.py",
                "-k",
                "TestUnit1.test_1"
            ]
        },
    ]
}
```

### 方法2
烧杯: 点击vscode左边的烧杯, 然后根据提示操作, 最终生成一个setting.json文件, 再次点击烧杯就可以调试了

第一步: launch.json中添加如下节点 或者 删除launch.json
```
        {
            "name": "py-break",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "purpose": ["debug-test"],
            "console": "integratedTerminal",
            "justMyCode": false,
        },

```
第二步: settings.json
```
{
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        "./tests",
        "-p",
        "test_*.py"
    ],
    "python.testing.pytestEnabled": false,
    "python.testing.unittestEnabled": true
}
```
