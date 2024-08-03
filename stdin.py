# cook your dish here
import sys

read = sys.stdin.readline
write = sys.stdout.write

MOD = 10**9 + 7

M, N = map(int, read().split())

ans = 0
for _ in range(N):
	x = int(read())
	ans = (ans + x) % MOD
	if M == 1:
		write(str(ans) + "\n")
if M == 0:
	write(str(ans) + "\n")