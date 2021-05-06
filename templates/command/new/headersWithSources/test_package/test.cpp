// include all hpp iles with full path eg. <HEM/Observer/Notifier.hpp>
#include <HEM/{{ name }}/DumpFile_please_replace_it_with_proper_source_files.hpp>

#include <iostream>
#include <functional>

std::function<void(void)> action = [](){
    std::cout << "Hello again from {{name}} package" << std::endl;
};

int main() {
	std::cout<<"Hello from {{ name }} package!" << std::endl;
	sayHello(action);
	return 0;
}
