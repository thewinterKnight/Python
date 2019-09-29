#include <iostream>
#include <vector>
#include <algorithm>

long long MaxPairwiseProductFast(const std::vector<long long>& numbers) {
	if (numbers.size() < 2)
		return 0;

	int max_indx1 = -1;
	int max_indx2 = -2;

	for (int index=0; index < numbers.size(); ++index) {
		if (numbers[index] > numbers[max_indx1] && index != max_indx2) {
			if (max_indx2 < 0 || numbers[max_indx1] > numbers[max_indx2]) {
				max_indx2 = max_indx1;
			}
			max_indx1 = index;
			continue;			
		}
		if (numbers[index] > numbers[max_indx2] && index != max_indx1) {
			if (max_indx1 < 0 || numbers[max_indx2] > numbers[max_indx1]) {
				max_indx1 = max_indx2;
			}
			max_indx2 = index;
			continue;
		}
	}

	// std::cout << max_indx1 << " & " << max_indx2 << "\n";

	if (max_indx1 < 0 || max_indx2 < 0) {
		return 0;
	}

	return numbers[max_indx1] * numbers[max_indx2];
}


long long MaxPairwiseProduct(const std::vector<long long>& numbers) {
    long long max_product = 0;
    int n = numbers.size();

    for (int first = 0; first < n; ++first) {
        for (int second = first + 1; second < n; ++second) {
            max_product = std::max(max_product, numbers[first] * numbers[second]);
        }
    }

    return max_product;
}

void StressTest() {
	int correct = 0;
    for (int j = 0; j < 500; ++j) {
    	int n = rand() % 1000;
    	std::vector<long long> numbers(n);
    	for (int i = 0; i < rand() % 10; ++i) {
    		// std::cout << "rand ... " << rand() % 1000 << "\n";
    		numbers[i] = (rand() % 1000000);
    	}

    	// if (j / 10 == 0) {
    	// 	std::cout << rand() % 100 << " : " << numbers[rand() % 100] << "\n";
    	// }

    	if (MaxPairwiseProduct(numbers) != MaxPairwiseProductFast(numbers)) {

    		for (int k = 0; k < 5; ++k) {
    			std::cout << numbers[k] << "\t";
    		}
    		std::cout << "\n";

    		std::cout << MaxPairwiseProduct(numbers) << " :: " << MaxPairwiseProductFast(numbers) << "\n";
    		std::cout << "Stress Test failed at " << correct << "\n";
    		return;
    	}
    	else {
    		std::cout << "PASS : " << MaxPairwiseProduct(numbers) << " :: " << MaxPairwiseProductFast(numbers) << "\n";
    	}
    	correct++;
	}
	std::cout << "Stress Test passed!" << "\n";
}

int main() {
    int n;
    std::cin >> n;
    std::vector<long long> numbers(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> numbers[i];
    }

    // StressTest();

    // std::cout << MaxPairwiseProduct(numbers) << "\n";
    std::cout << MaxPairwiseProductFast(numbers) << "\n";
    return 0;
}