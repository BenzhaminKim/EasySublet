import React, { useState } from 'react';
import {Link} from 'react-router-dom';

function PriceMarker({roomId,price}) {

  return (
    <a  className="btn btn-success" href={'http://localhost:8000/room/detail/'+roomId } >
      <b>$ {price}</b>
    </a>
  );
}

export default PriceMarker