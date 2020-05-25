#include <iostream>

using namespace std;

int main(){
	long long a, b, s, n, count;
	cin >> a >> b;
	count = 0;
	n = a;
	s = 0;
	while(n){
		s += n % 10;
		n /= 10;
	};
	if(s % 2 == 1){
		count +=  1;
	}
	for(long long i; i < b + 1; i++){
		if (i % 1000000000 == 0)
			s -= 9 * 9;
		else if (i % 100000000 == 0)
			s -= 9 * 8;
		else if (i % 10000000 == 0)
			s -= 9 * 7;
		else if (i % 1000000 == 0)
			s -= 9 * 6;
		else if (i % 100000 == 0)
			s -= 9 * 5;
		else if (i % 10000 == 0)
			s -= 9 * 4;
		else if (i % 1000 == 0)
			s -= 9 * 3;
		else if (i % 100 == 0)
			s -= 9 * 2;
		else if (i % 10 == 0)
			s -= 9;
		s += 1;
		if(s % 2 == 1)
			count += 1;
	}
	cout << count;
}