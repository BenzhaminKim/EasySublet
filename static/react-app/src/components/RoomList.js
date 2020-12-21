import React, { useState } from 'react';
import PageNation from './Pagenation';
import Room from './Room';

function RoomList() {
  // Declare a new state variable, which we'll call "count"
  const [count, setCount] = useState(0);

  return (
    <div >

        <div className="text-primary row m-2"><h3 className="col-12 text-center"> Rooms</h3></div>

        <div className="row m-0">
            <Room/>
            <Room/>
            <Room/>
            <Room/>
            <Room/>
            <Room/>
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