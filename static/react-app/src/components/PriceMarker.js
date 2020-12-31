import React, { useState } from 'react';

function PriceMarker({roomId,roomPrice}) {

  return (
    <a  className="row m-1" href={'http://localhost:8000/room/detail/'+roomId } >
        <button className="btn btn-success">
            <b>$ {roomPrice}</b>
        </button>
    </a>
  );
}

export default PriceMarker