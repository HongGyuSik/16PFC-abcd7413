#-*-coding:cp949
x = "There are %d of people." % 10 # 10���� ������� �ֽ��ϴ�.
binary = "binary" # ����
do_not = "don't" # ���� �ʴ´�.
y = "Those who know %s and those who %s." % (binary, do_not) #������ �ƴ� ������ �𸣴� ������� �ֽ��ϴ�.

print x # x���� ����Ѵ�.
print y # y���� ����Ѵ�.

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False # ����� = ����
joke_evaluation = "Isn't that joke so funny?! %r" # ����� = �� ����� ������� �ʴ�!?

print joke_evaluation % hilarious # ����� ������� ����Ѵ�.

w = "This the left side of..." # w = �̰��� ������ ����...
e = "a string with a right side." # e = ������ ���ڿ�.

print w + e # w + e�� ����Ѵ�.