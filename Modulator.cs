using System;
using System.Collections;
using System.Collections.Generic;

using UnityEngine;
using UnityOSC;



public class Modulator : MonoBehaviour {


    Vector3 tempPos;

    float data;
    //add or delete more objects to manipulate
    public GameObject hatake;
    
    //tester and New_data are used to modify the incoming data and debug the incoming data from strings to tester's data type
    float tester;
    string New_data;

    private Dictionary<string, ServerLog> servers;
    // Use this for initialization
    void Start () {
        OSCHandler.Instance.Init();

        servers = new Dictionary<string, ServerLog>();
         // Used to modify position of object in refrence
        tempPos = transform.position;

   
    }
	
	// Update is called once per frame
	void Update () {
        OSCHandler.Instance.UpdateLogs();
        servers = OSCHandler.Instance.Servers;
   
        foreach (KeyValuePair<string, ServerLog> item in servers)
        {
            // If we have received at least one packet,
            // show the last received from the log in the Debug console
            if (item.Value.log.Count > 0)
            {
                int lastPacketIndex = item.Value.packets.Count - 1;

                UnityEngine.Debug.Log(String.Format("SERVER: {0} ADDRESS: {1} VALUE 0: {2}",
                item.Key, // Server name
                item.Value.packets[lastPacketIndex].Address, // OSC address
                New_data=item.Value.packets[lastPacketIndex].Data[0].ToString())); //First data value
               // Debug.Log(New_data);
                //  Debug.Log(New_data);

                data= float.Parse(New_data, System.Globalization.CultureInfo.InvariantCulture);
           
            
                Debug.Log(data);
                // Do what you want with your data here, to manipulate your object
                transform.Rotate(Vector3.up * 15 * Time.deltaTime, Space.World);
            

            Debug.Log(tester);
                transform.position = tempPos;
             
            
            }
        }
        //Send OK
        if (Input.GetButtonDown("Fire1"))
        {
            OSCHandler.Instance.SendMessageToClient("FaceClient", "test/alive", "testing");
        }

    }
}
