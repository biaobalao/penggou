import openai

# OpenAI API 的密钥，用于在使用 OpenAI API 时进行身份验证和授权
openai.api_key = "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"
messages = []  # 将一个空列表 [] 赋值给变量 messages
'''print("您好，请输入接下来我需要扮演的角色。")
system_message = input("人类说：")

# messages是一个列表list结构，赋值对象是一个字典结构，append是列表的添加元素到结尾的方法
messages.append({"role": "system", "content": system_message})

print("好的，明白了! 如果想要结束当前对话您只需回复‘再见’即可。")'''

while True:
    # 收集用户的消息
    # print("\n")
    message = input("人类说：")
    # 这里的role是指角色的意思，然后role指的是用户，也就正在使用对话的那个人，然后content是指内容，值为我们输入的消息message
    messages.append({"role": "user", "content": message})

    '''
    ChatCompletion是OpenAI提供的一种基于机器学习的自然语言处理技术，可以根据用户输入的聊天内容，自动补全下一句话
    创建一个新的聊天对象，该方法接受任意数量的位置参数 *args 和关键字参数 **kwargs，cls 表示调用该方法的类本身
    temperature：用于控制生成文本的随机性，取值范围通常在 0 到 1 之间，较高的值会增加生成文本的多样性。
    max_tokens：指定生成的文本最大长度，以限制生成的回复长度。
    n：表示生成的文本数量，用于生成多个回复。
    stream：布尔值参数，用于指定是否以流式方式生成响应，即逐块生成回复而不是一次性生成完整的回复。
    logit_bias：用于调整生成文本的概率分布
    '''
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        # temperature=1,
        # stream=True
    )
    '''
    用于从一个 JSON 响应对象中提取特定字段的值，response是一个包含 JSON 数据的对象，通常是从某个 API 调用或其他数据源获取的响应
    choices是 JSON 响应对象中的一个字段或键，它可能包含一个数组或列表
    [0]表示选择数组或列表中的第一个元素
    message是所选第一个元素中的一个字段或键
    content是 message 字段中的一个字段或键，它可能包含需要提取的实际内容
    这种层次结构的访问方式常用于解析和提取复杂数据结构中的特定字段值
    通过逐步深入嵌套的对象和字段，可以访问到所需的具体数据
    '''
    reply = response["choices"][0]["message"]["content"]
    # print("\n")
    print("ChatGPT说: ", reply)

    match message.lower():
        case "再见":
            break
        case "see you":
            break
        case "goodbye":
            break
