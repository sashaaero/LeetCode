# https://leetcode.com/problems/DI String Match/
# Runtime: 160 ms, faster than 70.83% of Python3 online submissions for DI String Match
def di_string_match(s)
  l = s.length-1
  lo=0
  hi=l+1
  ans=[]
  (0..l).each do |i|
    if s[i].eql?('I')
      ans[i]=lo
      lo+=1
    else
      ans[i]=hi
      hi-=1
    end
  end
  ans[l+1]=lo
  return ans
end
