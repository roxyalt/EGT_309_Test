from useclass import ViltVQA
github_image = ViltVQA("https://github.githubassets.com/assets/github-mark-57519b92ca4e.png")

github_image._load_image()

question = "What is in this image?"
answer = github_image.ask(github_image.pil_img, question)

print(answer)