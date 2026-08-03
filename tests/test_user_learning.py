from engine.user_learning.learner import UserLearner

learner = UserLearner()

learner.learn("ọmọ")
learner.learn("ọmọ")
learner.learn("ọmọ")
learner.learn("ọmọkùnrin")
learner.learn("ọba")

print(learner.predict("ọ"))