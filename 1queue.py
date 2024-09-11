def enqueue(cus): # queue에 데이터를 추가하는 함수 정의
    q.append(cus) # queue에 cus를 추가
    
def dequeue(): # queue에서 데이터를 꺼내는 함수 정의
    if len(q) !=0: # queue에 데이터가 있는 경우
        cus = q.pop(0) # queue에 있는 데이터를 꺼내서 cus에 저장
        return cus # cus를 반환
    
def print_queue(): # queue에 있는 데이터를 출력하는 함수 정의
    for i in range(len(q)): # queue의 길이만큼 반복
        print('{!s:<8}'.format(q[i]), end='') 
        # queue의 i번째 데이터를 출력할 때 왼쪽 정렬 및 8자리 출력
    

q = [] # queue를 리스트로 선언

enqueue("고객1") # queue에 고객1 추가
enqueue("고객2") # queue에 고객2 추가
enqueue("고객3") # queue에 고객3 추가
print("1. 대기 중인 고객 :  ", end = '')
print_queue() # queue에 있는 데이터 출력
print("\n\n처리 중인 고객 :  ",dequeue()) # dequeue가 반환하는 데이터 출력
print("\n2. 대기 중인 고객 :  ", end='')
print_queue() # queue에 있는 데이터 출력


