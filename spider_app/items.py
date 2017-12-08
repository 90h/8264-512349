from scrapy import Item, Field


class PostItem(Item):
    floor = Field()  # 楼层
    content = Field()  # 内容
    created_at = Field()  # 创建时间

    screen_name = Field()  # 作者昵称
    avatar = Field()  # 作者头像
    space = Field()  # 作者空间
    reply_view = Field()  # 作者的所有回帖
    reply_count = Field()  # 回帖数
    online_count = Field()  # 在线时间
    registered_at = Field()  # 注册时间
