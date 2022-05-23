#include <string>
#include <cstring>
#include <cassert>
#include <iostream>
using namespace std;

#define c2i(v) v - '0'

int MOD = 1e9 + 7;

int dp[2001][2][2000];

int count(int m, int d, string a) {
  int N = a.size();
  memset(dp, 0, sizeof(dp));

  dp[0][0][0] = 1;
  for (int i = 0; i < N; i++) {
    int ai = c2i(a[i]);
    for (int smaller = 0; smaller < 2; smaller++) {
      for (int j = 0; j < m; j++) {
        for (int c = 0; c <= (smaller ? 9 : ai); c++) {
          if ((i % 2) == 0 && c == d)
            continue;
          if ((i % 2) == 1 && c != d)
            continue;
          if (i == 0 && c == 0)
            continue;
          int nsmaller = (smaller || c < ai) ? 1 : 0;
          int nj = (j * 10 + c) % m;
          dp[i+1][nsmaller][nj] = (
            dp[i+1][nsmaller][nj] +
            dp[i][smaller][j]
          ) % MOD;
        }
      }
    }
  }

  int ans = 0;
  for (int smaller = 0; smaller < 2; smaller++) {
    ans += dp[N][smaller][0];
    ans %= MOD;
  }

  return ans;
}

bool is_magic(int m, int d, string a) {
  int mod = 0;
  for (int i = 0; i < a.size(); i++) {
    int ai = c2i(a[i]);
    mod = (mod * 10 + ai) % m;
    if ((i % 2) == 0 && ai == d) {
      return false;
    }
    if ((i % 2) == 1 && ai != d) {
      return false;
    }
  }
  return mod == 0;
}


int solve(int m, int d, string a, string b) {
  return (
    count(m, d, b) - count(m, d, a) + MOD + (is_magic(m, d, a) ? 1 : 0)
  ) % MOD;
}

int main() {
  int m, d;
  string a, b;

  assert(solve(2, 6, "10", "99") == 8);
  assert(solve(2, 0, "1", "9") == 4);
  assert(solve(19, 7, "1000", "9999") == 6);

  cin >> m >> d >> a >> b;
  cout << solve(m, d, a, b);

  return 0;
}
