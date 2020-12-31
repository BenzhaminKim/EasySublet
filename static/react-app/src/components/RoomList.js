import axios from 'axios';
import React, { useState,useEffect,useRef } from 'react';
import PageNation from './Pagenation';
import Room from './Room';


function RoomList({rooms}) {
  return (
    <div >
        <div className="text-primary row m-2"><h3 className="col-12 text-center"> Rooms</h3></div>
        <div className="row m-0">
        {rooms.map(room => {
              return(
                  <Room key={room.id} roomId={room.id} price={room.price} title={room.title} images={room.images}/>
              );
          })}

        </div>
        <div className="row">
            <span className="col-lg-12 text-muted text-center font-italic border-top">
                    Rooms Everywhere Near You
            </span>
        </div>
    </div>
  );
}

export default RoomList