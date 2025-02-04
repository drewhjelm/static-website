from textnode import TextNode,TextType

def main():
    textnode = TextNode("Google",TextType.BOLD_TEXT,"http://google.com")
    print(textnode.__repr__())

main()