import os

os.system("docker run -it --detach -p 4873:4873 -v conf:/verdaccio/conf -v storage:/verdaccio/storage -v plugins:/verdaccio/plugins --name verdaccio verdaccio/verdaccio")
