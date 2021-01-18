import React, { useState } from 'react';

function PageNation() {
  // Declare a new state variable, which we'll call "count"
  const [count, setCount] = useState(0);

  return (
    <nav className="Page navigation col-lg-12 ml-3 mr-3 mb-1 mt-1">
        <ul className="pagination  justify-content-center">
            <li className="page-item">
                <a className="page-link" href="#" aria-label="Previous">
                    <span aria-hidden="true"><i className="fas fa-arrow-left"></i></span>
                </a>
            </li>
            <li className="page-item"><a className="page-link"  href="#">this.state.firstPage</a></li>
            <li className="page-item"><b className="page-link" href="#"><i className="fas fa-ellipsis-h"></i></b></li>
            <li className="page-item"><a className="page-link"  href="#">this.state.lastPage</a></li>
            <li className="page-item">
                <a className="page-link" href="#"  aria-label="Next">
                    <span aria-hidden="true"><i className="fas fa-arrow-right"></i></span>
                </a>
            </li>
        </ul>
    </nav>
  );
}

export default PageNation