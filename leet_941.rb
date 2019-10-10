# https://leetcode.com/problems/valid-mountain-array/
# Runtime: 52 ms, faster than 73.08% of ruby online submissions for valid-mountain-array.

def valid_mountain_array(a)
  l = a.length
  if l < 3
    return false
  else
    l=l
    i=0
    while(i+1<l && a[i] < a[i+1])
     i+=1
    end
   if i.eql?(0) || i.eql?(l-1)
     return false
   end
   while(i+1<l && a[i+1] < a[i])    
     i+=1
   end
  end
  return i.eql?(l-1)
end
