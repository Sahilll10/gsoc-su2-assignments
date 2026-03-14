import pysu2
import math
from mpi4py import MPI

def main():
    comm = MPI.COMM_WORLD
    SU2Driver = pysu2.CSinglezoneDriver('unsteady_CHT_FlatPlate_Conf.cfg', 1, comm)

    CHTMarkerList = SU2Driver.GetCHTMarkerTags()
    allMarkerIDs = SU2Driver.GetMarkerIndices()
    print("CHT Markers:", CHTMarkerList)

    MarkerID = None
    for tag in CHTMarkerList:
        if tag in allMarkerIDs:
            MarkerID = allMarkerIDs[tag]
            MarkerTag = tag
            break

    if MarkerID is None:
        print("No CHT marker found")
        SU2Driver.Finalize()
        return

    nVertex = SU2Driver.GetNumberMarkerNodes(MarkerID)
    print(f"Using marker '{MarkerTag}' with {nVertex} vertices")

    for iTimeIter in range(10):
        for iVertex in range(nVertex):
            x = SU2Driver.MarkerCoordinates(MarkerID)(iVertex, 0)
            T_wall = 300.0 + 50.0 * math.sin(2 * math.pi * x / 0.5)
            SU2Driver.SetMarkerCustomTemperature(MarkerID, iVertex, T_wall)
        SU2Driver.BoundaryConditionsUpdate()
        SU2Driver.Run()
        SU2Driver.Output(iTimeIter)
        SU2Driver.Update()
        print(f"Time iter {iTimeIter} done")

    SU2Driver.Finalize()

if __name__ == '__main__':
    main()
