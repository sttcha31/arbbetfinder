#include "Bookie.hpp"
#include <thread>
#include <iostream>
#include <Python.h>
#include <fstream>
#include <vector>

using namespace std;

void call_python_function(const string& module_name, const string& function_name) {
     PyObject* pModule = PyImport_ImportModule(module_name.c_str());
    if (pModule == nullptr) {
        PyErr_Print();
        return;
    }
    PyObject* pFunc = PyObject_GetAttrString(pModule, function_name.c_str());
    if (pFunc == nullptr) {
        PyErr_Print();
        return;
    }
    PyObject* pResult = PyObject_CallObject(pFunc, nullptr);
    if (pResult == nullptr) {
        PyErr_Print();
        return;
    }
    Py_DECREF(pResult);
    Py_DECREF(pFunc);
    Py_DECREF(pModule);
}

int main() {
    // Py_Initialize();

    // vector<thread> threads;
    // ifstream fin("mgmgames.txt");
    // string line;
    // if(fin.is_open()) {
    //     while (getline(fin, line)) {
    //         cout << line << endl;
    //         threads.push_back(thread(call_python_function, ""));
    //     }
    //     fin.close(); 
    // }

    // for (auto& th : threads) {
    //     th.join();
    // }
    // Py_Finalize(); 
    // return 0;
    Py_Initialize();

    PyObject* sysPath = PySys_GetObject("path");
    PyObject* currentDir = PyUnicode_FromString(".");
    PyList_Append(sysPath, currentDir);
    Py_DECREF(currentDir);
    call_python_function("betmgm_scraper", "get_game_links");
    // // Import the Python module
    // PyObject* pModule = PyImport_ImportModule("my_module");
    // if (pModule == nullptr) {
    //     PyErr_Print();
    //     return 1;
    // }

    // // Get the function from the module
    // PyObject* pFunc = PyObject_GetAttrString(pModule, "my_function");
    // if (pFunc == nullptr) {
    //     PyErr_Print();
    //     return 1;
    // }

    // // Call the function with arguments
    // PyObject* pArgs = PyTuple_New(2);
    // PyTuple_SetItem(pArgs, 0, PyLong_FromLong(10));
    // PyTuple_SetItem(pArgs, 1, PyLong_FromLong(20));

    // PyObject* pResult = PyObject_CallObject(pFunc, pArgs);
    // if (pResult == nullptr) {
    //     PyErr_Print();
    //     return 1;
    // }

    // // Convert the result to a C++ type
    // long result = PyLong_AsLong(pResult);
    // std::cout << "Result: " << result << std::endl;
    // // Clean up
    // Py_DECREF(pArgs);
    // Py_DECREF(pResult);
    // Py_DECREF(pFunc);
    // Py_DECREF(pModule);
    Py_Finalize();

    return 0;
}


// g++ -std=c++17 -o main.exe  main.cpp -I/Library/Frameworks/Python.framework/Versions/3.13/include/python3.13
// clang++ -o main.exe  main.cpp -I/Library/Frameworks/Python.framework/Versions/3.13/include/python3.13
// g++ -std=c++11 -o main.exe main.cpp -I/Library/Frameworks/Python.framework/Versions/3.13/include/python3.13

// clang -std=c++17 -lstdc++ -o main.exe main.cpp -I/Library/Frameworks/Python.framework/Versions/3.13/include/python3.13 -lpython3.13 -L/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/config-3.13-darwin

// ./main.exe 
