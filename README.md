python-socketio/tornadoでroomを使うサンプル


1. `python ./simple/app.py`
2. `http://localhost:8888` を開く (A)
3. `current` メッセージを受信 (A)
4. `update` メッセージを送信 (A)
3. `http://localhost:8888` を開く (B)
3. `current` メッセージを受信 (B)
4. `update` メッセージを送信 (B)
5. `update` メッセージを受信 (A)

※ デバッグコンソールを開いてください。

公式サンプル: https://github.com/miguelgrinberg/python-socketio/tree/master/examples/server/tornado

* `simple/app.py`: Tornado & `Socket.io`
* `simple/sio.py`: クエリ`room_id`で指定された`room`に`join`し、`update`や`Socket.io`イベント処理
* `simple/room.py`: `room`データ管理のスタブ
* `multiroom/`: 複数`room`のサンプル
