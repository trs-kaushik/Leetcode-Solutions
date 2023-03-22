#Print all subsequences
def subsequence_sum(ind, stack, sum, seq,trgt):
        if ind == len(seq):
                if sum == trgt:
                        print(stack)
                return
        stack.append(seq[ind])
        sum+=seq[ind]
        subsequence_sum(ind+1, stack,sum,seq,trgt)
        temp = stack.pop()
        sum-=temp
        subsequence_sum(ind+1, stack, sum, seq,trgt)

subsequence_sum(0,[],0,[1,2,1],3)



#Stop after one satisfying subsequence
def subsequence_sum(ind, stack, sum, seq,trgt):
        if ind == len(seq):
                if sum == trgt:
                        print(stack)
                        return True
                else:
                        return False
                        
        stack.append(seq[ind])
        sum+=seq[ind]
        res_left = subsequence_sum(ind+1, stack,sum,seq,trgt)
        if res_left:
                return True
        temp = stack.pop()
        sum-=temp
        res_right = subsequence_sum(ind+1, stack, sum, seq,trgt)
        if res_right:
                return True
                
        return False

print(subsequence_sum(0,[],0,[1,2,1],5))


#Combination sum 1
#Print all subsequences
def subsequence_sum(ind, stack, sum, seq,trgt):
        if ind == len(seq):
                if sum == trgt:
                        print(stack)
                        return True
                else:
                        return False
        if sum > trgt:
                return False
        elif sum==trgt:
                print(stack)
                return True
                
        stack.append(seq[ind])
        sum+=seq[ind]
        left = subsequence_sum(ind, stack,sum,seq,trgt)
        temp = stack.pop()
        sum-=temp
        right = subsequence_sum(ind+1, stack, sum, seq,trgt)
        
        return left and right

subsequence_sum(0,[],0,[2,3,5],8)



#Combination SUm 2:
def findcombination(ind, target, arr, stack):
        if target == 0:
                print(stack)
                return 
        for i in range(ind, len(arr)):
                if (i>ind and arr[i]==arr[i-1]): continue
                if (arr[i] > target): break
                stack.append(arr[i])
                findcombination(i+1, target-arr[i], arr, stack)
                stack.pop()

findcombination(0,5,sorted([2,5,2,1,2]),[])
