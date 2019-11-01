class Solution {
public:
  int countPrimeSetBits(int L, int R) {
    int ans = 0;
    for (int n = L; n <= R; ++n)
      if (isPrime(bits(n))) ++ans;
    return ans;
  }
private:
  bool isPrime(int n) {
    if (n <= 1) return false;
    if (n == 2) return true;      
    for (int i = 2; i <= sqrt(n); ++i)
      if (n % i == 0) return false;
    return true;
  }
  
  int bits(int n) {
    int s = 0;
    while (n) {
      s += n & 1;
      n >>= 1;
    }        
    return s;
  }
};
