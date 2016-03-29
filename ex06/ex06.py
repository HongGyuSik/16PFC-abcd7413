#-*-coding:cp949
x = "There are %d of people." % 10 # 10명의 사람들이 있습니다.
binary = "binary" # 진수
do_not = "don't" # 하지 않는다.
y = "Those who know %s and those who %s." % (binary, do_not) #진수를 아는 사람들과 모르는 사람들이 있습니다.

print x # x값을 출력한다.
print y # y값을 출력한다.

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False # 들썩들썩 = 실패
joke_evaluation = "Isn't that joke so funny?! %r" # 농담평가 = 그 농담은 재미있지 않니!?

print joke_evaluation % hilarious # 농담평가 들썩들썩을 출력한다.

w = "This the left side of..." # w = 이것은 왼쪽의 측면...
e = "a string with a right side." # e = 우측의 문자열.

print w + e # w + e를 출력한다.