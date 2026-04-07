def markdown_to_blocks(markdown) -> list:
    blocks = markdown.strip().split("\n\n")
    result = []
    for block in blocks:
        block = block.strip()
        if block != "":
            result.append(block)
    return result
