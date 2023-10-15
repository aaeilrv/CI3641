#include <iostream>
#include <cmath>
using namespace std;

// Definición del namespace
namespace vector3D
{
    struct Vector {
        double x, y, z;
    };

    //// SUMA ////

    // dos vectores
    Vector operator+(const Vector& a, const Vector& b)
    {
        return Vector{a.x + b.x, a.y + b.y, a.z + b.z};
    }

    // vector y escalar
    Vector operator+(const Vector& a, double scalar) {
        return {a.x + scalar, a.y + scalar, a.z + scalar};
    }

    //// RESTA ////

    // dos vectores
    Vector operator-(const Vector& a, const Vector& b)
    {
        return Vector{a.x - b.x, a.y - b.y, a.z - b.z};
    }

    // vector y escalar
    Vector operator-(const Vector& a, double scalar)
    {
        return Vector{a.x - scalar, a.y - scalar, a.z - scalar};
    }

    //// PRODUCTO CRUZ ////

    // Dos vectores
    Vector operator*(const Vector&a, const Vector& b)
    {
        double x = a.y * b.z - a.z * b.y;
        double y = a.z * b.x - a.x * b.z;
        double z = a.x * b.y - a.y * b.x;

        return Vector{x, y, z};
    }

    // Vector y escalar
    Vector operator*(const Vector& a, double scalar)
    {
        double x = a.y * scalar - a.z * scalar;
        double y = a.z * scalar - a.x * scalar;
        double z = a.x * scalar - a.y * scalar;

        return Vector{x, y, z};
    }

    //// PRODUCTO PUNTO ////

    // Dos vectores
    double operator%(const Vector& a, const Vector& b)
    {
        return a.x * b.x + a.y * b.y + a.z * b.z;
    }

    //// NORMA ////
    double operator&(const Vector& a)
    {
        return std::sqrt(a.x * a.x + a.y * a.y + a.z * a.z);
    }

    // Impresión del vector
    std::string to_string(const Vector& v) {
        return "(" + std::to_string(v.x) + ", " + std::to_string(v.y) + ", " + std::to_string(v.z) + ")";
    }
}

using namespace vector3D;

int main()
{
    Vector a = {1, 2, 3};
    Vector b = {6, -10, -1};
    Vector c = {-3, -2, 5};

    Vector res = b + c;
    Vector res1 = a * b - c;
    Vector res2 = (b + b) * (c - a);
    double res3 = a % (c * b);

    Vector res4 = b + 3;
    Vector res5 = a * 3 + b;
    Vector res6 = (b + b) * (c % a);

    std::cout << "Suma (b + c): " << to_string(res) << "\n";
    std::cout << "a * b - c: " << to_string(res1) << "\n";
    std::cout << "(b + b) * (c - a): " << to_string(res2) << "\n";
    std::cout << "a % (c * b): " << to_string(res3) << "\n";

    std::cout << "b + 3: " << to_string(res4) << "\n";
    std::cout << "a * 3 + b: " << to_string(res5) << "\n";
    std::cout << "(b + b) * (c \% a): " << to_string(res6) << "\n";
}