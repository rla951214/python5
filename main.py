from animal import dog # animal 패키지에서 dog 라는 모듈을 가져온다.
from animal import cat # animal 패키지에서 cat 이라는 모듈을 가져온다.
from animal import horse # animal 패키지에서 horse 라는 모듈을 가져온다.
from animal import snake # animal 패키지에서 snake 라는 모듈을 가져온다.

from animal import * # animal 패키지가 갖고 있는 모듈을 다 불러온다.

d = Dog()
c = Cat()
h = Horse()
s = Snake()

d.hi()
c.hi()
h.hi()
s.hi()