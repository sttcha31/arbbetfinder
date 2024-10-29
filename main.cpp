#include "Bookie.hpp"
#include <thread>
#include <iostream>
#include <Python.h>
#include <fstream>
#include <vector>

using namespace std;
void call_python_function(const char* module_name, const char* function_name, const char* link, const char* category) {
    // Acquire the GIL
    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();

    // Import the Python module
    PyObject* pName = PyUnicode_DecodeFSDefault(module_name);
    PyObject* pModule = PyImport_Import(pName);
    Py_DECREF(pName);

    if (pModule != nullptr) {
        // Get the Python function
        PyObject* pFunc = PyObject_GetAttrString(pModule, function_name);
        if (pFunc && PyCallable_Check(pFunc)) {
            // Call the Python function (no arguments here)
            PyObject* pValue = PyObject_CallObject(pFunc, nullptr);
            if (pValue != nullptr) {
                std::cout << "Python function call successful!" << std::endl;
                Py_DECREF(pValue);
            } else {
                PyErr_Print();
                std::cerr << "Call failed." << std::endl;
            }
        } else {
            PyErr_Print();
            std::cerr << "Cannot find function." << std::endl;
        }
        Py_XDECREF(pFunc);
        Py_DECREF(pModule);
    } else {
        PyErr_Print();
        std::cerr << "Failed to load module." << std::endl;
    }

    // Release the GIL
    PyGILState_Release(gstate);
}

int main() {
    Py_Initialize();
    PyEval_InitThreads();

    int numthreads;
    vector<thread> threads;
    ifstream fin("mgmgames.txt");
    string line;
    if(fin.is_open()) {
        while (getline(fin, line)) {  // Read the file line by line
            cout << line << endl;  // Print each line to the console
            threads.push_back(thread('betmgm_scraper.py', 'get_player_overunder', line, "Points"));
        }
        fin.close(); 
    }

     for (auto& th : threads) {
        th.join();
    }
    Py_Finalize(); 
    return 0;

}

// g++ -o main.exe  main.cpp -I/Library/Frameworks/Python.framework/Versions/3.13/include/python3.13
// ./main.exe 
