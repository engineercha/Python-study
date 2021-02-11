import time
print(print(time.localtime()),"\n")
print("코로나바이러스감염증-19 (COVID-19)")
print("2021-02-11 00:00 기준\n")

cases_in = 82434
test_in = 81614
lift_in = 72638
deaths_in = 1496

cases_ex = 107339132
deaths_ex = 2354414

print("\n<국내현황>")
print("확진환자", cases_in)
print("검사중  ", test_in)
print("격리해제", lift_in)
print("사망자  ", deaths_in)

print("\n<세계현황>")
print("확진환자", cases_ex)
print("사망자  ", deaths_ex)

print("\n세계 대비 국내 확진환자 비율:",cases_in/cases_ex*100,"%")
print("세계 대비 국내   사망자 비율:",deaths_in/deaths_ex*100,"%")

drate_in = deaths_in/cases_in*100
drate_ex = deaths_ex/cases_ex*100
print('\n국내 치명률: %.3f'%drate_in,"%") 
print('세계 치명률: %.3f'%drate_ex,"%")

if deaths_in/cases_in*100 > deaths_ex/cases_ex*100:
    print("국내 치명률은 세계 치명률 보다 약",drate_in - drate_ex,"% 높습니다")
elif deaths_in/cases_in*100 < deaths_ex/cases_ex*100:
    print("국내 치명률은 세계 치명률 보다 약",drate_ex - drate_in,"% 낮습니다.")
else: print("국내 치명률은 세계 치명률과 같습니다.")