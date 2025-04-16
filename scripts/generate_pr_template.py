import sys

title = sys.argv[1]

print(f"""## :star2: やったこと (必須。1行で簡潔に)
{title}

## :mag_right: 詳細 (必須)


## :bug: 確認したこと (必須)
- [ ] xxx

## :memo: 関連リンク


## :art: UI 差分
|BEFORE|AFTER|
|:--:|:--:|
|<img width="300" src=""/>|<img width="300" src=""/>|
""")
