import React, { useState,useEffect } from 'react';
import GoogleMap from './googleMap.js';
import RoomList from './RoomList.js';
import axios from 'axios';

export default function App() {
    const [bounds,setBounds] = useState({nw:{lat:0,lng:0},se:{lat:0,lng:0},sw:{lat:0,lng:0},ne:{lat:0,lng:0}});
    const [rooms,setRooms] = useState([]);

    const fetchRooms=()=>{
        axios.get(`http://localhost:8000/api/room/list`,{
                params: {
                    nw_lat : bounds.nw.lat,
                    nw_lng : bounds.nw.lng,
                    se_lat : bounds.se.lat,
                    se_lng : bounds.se.lng
                        }
                }).then(response => {
                    setRooms(response.data);
                    
            });
    }
    
    useEffect(()=>{
        fetchRooms();
    },[bounds]);


    return (
        <div className="row" style={{ width: '100%' }}>
            <div className="col-3">
                <RoomList rooms={rooms} />
            </div>
            <div className="col-9">
                <GoogleMap onChange={(bounds)=>{
                    setBounds(bounds);
                }}/>
            </div>
        </div>
    );
    
}