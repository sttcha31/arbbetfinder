#include "Bookie.hpp"
#include <thread>
#include <iostream>
#include <Python.h>
#include <fstream>
#include <vector>
#include <unordered_map>

using namespace std;
// class ArbFinder {
//     public:
//         ArbFinder() {}

//         void call_python_function(const string& module_name, const string& function_name, vector<string> arguments) {
//             PyObject* pModule = PyImport_ImportModule(module_name.c_str());
//             if (pModule == nullptr) {
//                 PyErr_Print();
//                 return;
//             }
//             PyObject* pFunc = PyObject_GetAttrString(pModule, function_name.c_str());
//             if (pFunc == nullptr) {
//                 PyErr_Print();
//                 return;
//             }
//             PyObject* pResult;
//             PyObject* pArgs = PyTuple_New(arguments.size());
//             for(int i = 0; i < arguments.size(); ++i){
//                 PyTuple_SetItem(pArgs, i, PyUnicode_FromString(arguments[i].c_str()));
//             }
//             pResult = PyObject_CallObject(pFunc, pArgs);
//             if (pResult == nullptr) {
//                 PyErr_Print();
//                 return;
//             }
//             PyObject* keys = PyDict_Keys(pResult);
//             if (keys != nullptr) {
//                 Py_ssize_t size = PyList_Size(keys); // Number of items in the dictionary
//                 for (Py_ssize_t i = 0; i < size; ++i) {
//                     // Get key and value
//                     PyObject* key = PyList_GetItem(keys, i);
//                     PyObject* value = PyDict_GetItem(pResult, key);

//                     // Convert the key to a string
//                     const char* keyStr = PyUnicode_AsUTF8(key);
//                     std::cout << keyStr << ": ";

//                     // Check if the value is a tuple
//                     if (PyTuple_Check(value)) {
//                         std::cout << "(";
//                         Py_ssize_t tupleSize = PyTuple_Size(value);
//                         for (Py_ssize_t j = 0; j < tupleSize; ++j) {
//                             PyObject* item = PyTuple_GetItem(value, j);
//                             if (PyUnicode_Check(item)) {
//                                 const char* itemStr = PyUnicode_AsUTF8(item);
//                                 std::cout << itemStr;
//                             }
//                             if (j < tupleSize - 1) std::cout << ", ";
//                         }
//                         std::cout << ")";
//                     } else {
//                         std::cout << "(unexpected type)";
//                     }
//                     std::cout << std::endl;
//                 }
//             }
//             Py_DECREF(pResult);
//             Py_DECREF(pFunc);
//             Py_DECREF(pModule);
//         }
//     private:
//         unordered_map<pair<string, string>, vector<Bookie*>> hashMap;

// };

void call_python_function(const string& module_name, const string& function_name, vector<string> arguments) {
    PyGILState_STATE gstate = PyGILState_Ensure();

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
    PyObject* pResult;
    PyObject* pArgs = PyTuple_New(arguments.size());
    for(int i = 0; i < arguments.size(); ++i){
        PyTuple_SetItem(pArgs, i, PyUnicode_FromString(arguments[i].c_str()));
    }
    pResult = PyObject_CallObject(pFunc, pArgs);
    if (pResult == nullptr) {
        PyErr_Print();
        return;
    }
    PyObject* keys = PyDict_Keys(pResult);
    if (keys != nullptr) {
        Py_ssize_t size = PyList_Size(keys); // Number of items in the dictionary
        for (Py_ssize_t i = 0; i < size; ++i) {
            // Get key and value
            PyObject* key = PyList_GetItem(keys, i);
            PyObject* value = PyDict_GetItem(pResult, key);

            // Convert the key to a string
            const char* keyStr = PyUnicode_AsUTF8(key);
            std::cout << keyStr << ": ";

            // Check if the value is a tuple
            if (PyTuple_Check(value)) {
                std::cout << "(";
                Py_ssize_t tupleSize = PyTuple_Size(value);
                for (Py_ssize_t j = 0; j < tupleSize; ++j) {
                    PyObject* item = PyTuple_GetItem(value, j);
                    if (PyUnicode_Check(item)) {
                        const char* itemStr = PyUnicode_AsUTF8(item);
                        std::cout << itemStr;
                    }
                    if (j < tupleSize - 1) std::cout << ", ";
                }
                std::cout << ")";
            } else {
                std::cout << "(unexpected type)";
            }
            std::cout << std::endl;
        }
    }
    Py_DECREF(pResult);
    Py_DECREF(pFunc);
    Py_DECREF(pModule);
    PyGILState_Release(gstate); 
}

void get_links(const string& module_name, const string& function_name) {
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

    Py_Initialize();

    PyObject* sysPath = PySys_GetObject("path");
    PyObject* currentDir = PyUnicode_FromString(".");
    PyList_Append(sysPath, currentDir);
    Py_DECREF(currentDir);
    // vector<string> args = {"https://sports.mi.betmgm.com/en/sports/events/minnesota-timberwolves-at-boston-celtics-16529704", "points"};
    // call_python_function("betmgm_scraper", "get_player_overunder", args);

    vector<thread> threads;
    ifstream fin("mgmgames.txt");
    string line;
    if(fin.is_open()) {
        while (getline(fin, line)) {
            cout << line << endl;
            vector<string> args = {line, "points"};
            call_python_function("betmgm_scraper", "get_player_overunder", args);
            // threads.push_back(thread(call_python_function, "betmgm_scraper", "get_player_overunder", args));
        }
        fin.close(); 
    }

    // for (auto& th : threads) {
    //     cout << "hi" << endl;
    //     th.join();
    // }

    Py_Finalize();

    return 0;
}


// g++ -std=c++17 -o main.exe  main.cpp -I/Library/Frameworks/Python.framework/Versions/3.13/include/python3.13
// clang++ -o main.exe  main.cpp -I/Library/Frameworks/Python.framework/Versions/3.13/include/python3.13
// g++ -std=c++11 -o main.exe main.cpp -I/Library/Frameworks/Python.framework/Versions/3.13/include/python3.13

// clang -std=c++17 -lstdc++ -o main.exe main.cpp -I/Library/Frameworks/Python.framework/Versions/3.13/include/python3.13 -lpython3.13 -L/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/config-3.13-darwin

// ./main.exe 
