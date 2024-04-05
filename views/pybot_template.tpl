<html>
<head>
<title>「地震」と言ったら反応するChatBot</title>
<style type="text/css">
li {
    font-size: 20px;
    font-weight:  bold;
}
.data_li{
    color : #303070;
}
</style>
</head>
<body>
<h1>pybot Webアプリケーション</h1>
<h2>「地震」と言ったら反応するChatBot</h2>
<form method="post" action="/hello">
メッセージを入力してください: <input type="text" name="input_text">
<input type="submit" value="送信">
</form>
    <ul>
        <li>入力:   {{input_text}}</li>

    </ul>
% if list_flag:
    <ul>
        <li>pybotからの応答メッセージ: </li>
    </ul>m
    <ul class="data_ul">
    % for recordlist in output_text:
        <li class="data_li">{{recordlist[0]}}
            {{recordlist[1]}}|<a href="/{{recordlist[2]}}">地図</a></li>
    % end
    </ul>
% else:
    <ul>
        <li>pybotからの応答メッセージ: {{output_text}}</li>
    </ul>
% end
</body>
</html>
