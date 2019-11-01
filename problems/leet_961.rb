# https://leetcode.com/problems/N-Repeated Element in Size 2N Array/
# Runtime: 48 ms, faster than 81.88% of ruby online submissions for N-Repeated Element in Size 2N Array
def repeated_n_times(a)
  ans = Hash.new(0)
  a.each do |k|
    if ans[k] > 1
      return k
    else
      ans[k] +=1
    end
  end
  return ans.max_by{|k,v| v}[0]
end
