import re
import copy

def mul(x):
    ans = 1
    for i in x:
        ans = ans*int(i)
    return ans

def div(x):
    ans = int(x[0])
    x = x[1:]
    for i in x:
        ans = ans/int(i)
        ans = int(ans)
    return ans

def add_sub(x,y): #x为所有的数字，y为所有的负数
    ans = 0
    for i in x:
        ans = ans+int(i)
    for i in y:
        ans = ans+2*int(i) #负号可以通过强制转换生效
    return ans

def list_reverse(x):
    length = len(x)
    ans = [None]*length
    for i in x:
        length =length - 1
        ans[length] = i
    return ans

def mul_step(bracket_first):
    #bracket_first_replace = copy.deepcopy(bracket_first)
    length_eql = 0
    # (1+9*2*1*1*1)---》['9', '2', '1', '1', '1'] 列表for循环
    #(1+9*2*1*1*1/9*2*1)
    for i in bracket_first:
        equal_mul = re.findall('\d+\*[^+-/]*\d+',i) #存储每个底层括号内的式子,也是最后要被替换掉的元素
        #[9*2*1,9*2*1*1*1] equal_mul
        for j in equal_mul:
            element_mul = re.findall('\d+',j) #取出乘法式子中所有的元素
            equal_ans = str(mul(element_mul))
            if not last_flag:   # 用于最后一次运算的特殊情况
                bracket_first[0] = bracket_first[0].replace(j,equal_ans,1)
                return bracket_first
            else:
                bracket_first_replace[length_eql] = bracket_first_replace[length_eql].replace(j, equal_ans,1)
        #equal_ans [18,18]
        length_eql += 1
    return bracket_first_replace

def div_step(bracket_first):
    length_eql = 0
    for i in bracket_first:
        equal_mul = re.findall('\d+/[^*+-]*\d+',i) #存储每个底层括号内的式子,也是最后要被替换掉的元素
        for j in equal_mul:
            element_mul = re.findall('\d+',j) #取出乘法式子中所有的元素
            equal_ans = str(div(element_mul))
            if not last_flag:
                bracket_first[0] = bracket_first[0].replace(j,equal_ans,1)
                return bracket_first
            else:
                bracket_first_replace[length_eql] = bracket_first_replace[length_eql].replace(j, equal_ans,1)
        length_eql += 1
    return bracket_first_replace

def add_sub_step(bracket_first):
    length_eql = 0
    for i in bracket_first:
        temp = re.findall('[^()]+',i)
        for j in temp:
            num_all = re.findall('\d+',j) #找出所有的数
            num_neg = re.findall('-\d+',j) #找出所有的负数
            equal_ans = add_sub(num_all,num_neg) #算出答案
            if not last_flag:
                return equal_ans
            else:
                bracket_first_replace[length_eql] = str(equal_ans)
        length_eql += 1
    return bracket_first_replace

a = "1+((1+1+1)+81/9/3)*2+(2+(9-81/9/3*1/3))/2+(   1+9*2*1*1*1/9*2*1)"

equ = a.replace(' ','')
print(equ)
i = 3
last_flag = True

while last_flag:
    bracket_first = re.findall('\([^()]+\)',equ) #提取最先括号里的元素
    bracket_first_replace = copy.deepcopy(bracket_first)
    # bracket_first_replace1 = mul_step(bracket_first) #过滤乘法
    # bracket_first_replace2 = div_step(bracket_first_replace1)
    bracket_first_replace = add_sub_step(div_step(mul_step(bracket_first)))
    print(bracket_first)
    print(bracket_first_replace)
    length = len(bracket_first_replace)

    for i in range(length):
        equ = equ.replace(bracket_first[i],bracket_first_replace[i],1)

    print(equ)
    last_flag = re.findall('[()]',equ)

least_equ = [equ]
Ans_final = add_sub_step(div_step(mul_step(least_equ)))
print(Ans_final)