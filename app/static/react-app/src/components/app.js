import React, { useState,useEffect } from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
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
        <Router>
            <div className="row m-0" style={{ width: '100%' }}>
                <div className="col-4 p-0 scroll-container">
                    <RoomList rooms={rooms} />
                </div>
                <div className="col-8 p-0">
                    <GoogleMap onChange={(bounds)=>{
                        setBounds(bounds);
                    }}/>
                </div>
            </div>
        </Router>
    );
    
}