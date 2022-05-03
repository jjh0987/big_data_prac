import pandas as pd
test = pd.read_csv('/Users/junho/Downloads/카카오뉴스기사_최종.csv')
test.columns
test.info()
from transformers import pipeline
zs = pipeline('zero-shot-classification')

##########
score = []
label = ['price rise','price drop']
cnt = 0
for sequence in list(test['영문번역']):
    temp = zs(sequence,label)
    temp_score = abs(temp['scores'][0]-temp['scores'][1])
    cnt += 1

    if temp['labels'][0] == 'fear':
        score.append(-temp_score)
        print(f'{cnt}/{len(test)}' + f': append -{temp_score}')
    else:
        score.append(temp_score)
        print(f'{cnt}/{len(test)}' + f': append {temp_score}')

test['price_rise/price_drop'] = score
test.to_csv('/Users/junho/Downloads/카카오뉴스기사_최종.csv')

###########

qa = pipeline("question-answering")
question = 'Is the stock of the Kakao Company going up?' # 답변을 레이블에 맞춰서 나오도록 유도하는 질문 ex)당신은 두렵습니까?
label = ['fear','greed'] # 수정 가능 ex) 가격상승/하락
qa_score = []
cnt = 0
for i in range(len(test)):
    cnt += 1
    ans = qa(question = question, context = test.loc[i,'영문번역'])
    temp = zs(ans['answer'],label)
    temp_score = abs(temp['scores'][0]-temp['scores'][1])
    print(ans)

    if temp['labels'][0] == 'fear':
        qa_score.append(-temp_score)
        print(f'{cnt}/{len(test)}' + f': append -{temp_score}')
    else:
        qa_score.append(temp_score)
        print(f'{cnt}/{len(test)}' + f': append {temp_score}')
