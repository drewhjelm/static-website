from textnode import TextNode,TextType

def main():
    textnode = TextNode("Google",TextType.BOLD,"http://google.com")
    print(textnode.__repr__())

if __name__ == "__main__":
    main()