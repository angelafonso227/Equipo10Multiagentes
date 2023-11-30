using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ATransRuedas : MonoBehaviour
{
    [SerializeField] Vector3 displacement;
    [SerializeField] float angle;
    [SerializeField] AXIS rotationAxis;
    Mesh mesh;
    Vector3[] baseVertices;
    Vector3[] newVertices;

    // Start is called before the first frame update
    void Start()
    {
        mesh = GetComponent<MeshFilter>().mesh;
        baseVertices = mesh.vertices;

        // Crear una copia de los vértices originales
        newVertices = new Vector3[baseVertices.Length];
        for (int i = 0; i < baseVertices.Length; i++)
        {
            newVertices[i] = baseVertices[i];
        }
    }

    // Update is called once per frame
    void Update()
    {
        DoTransform();
    }

    void DoTransform()
    {
        // Matriz de traslación en función del tiempo multiplicado por el desplazamiento
        Matrix4x4 move = HW_Transforms.TranslationMat(displacement.x * Time.time, displacement.y * Time.time, displacement.z * Time.time);

        // Matriz de rotación en función del tiempo multiplicado por el ángulo y el eje de rotación
        Matrix4x4 rotate = HW_Transforms.RotateMat(angle * Time.time, rotationAxis);

        // Matriz compuesta de traslación y rotación
        Matrix4x4 composite = move * rotate;

        // Aplicar la transformación a cada vértice del objeto
        for (int i = 0; i < newVertices.Length; i++)
        {
            // Crear un vector temporal con las coordenadas del vértice original
            Vector4 temp = new Vector4(baseVertices[i].x, baseVertices[i].y, baseVertices[i].z, 1);
            // Aplicar la transformación a cada vértice
            newVertices[i] = composite * temp;
        }

        // Reemplazar los vértices en el objeto de malla
        mesh.vertices = newVertices;

        // Recalcular las normales de la malla
        mesh.RecalculateNormals();
    }
}
